import argparse
from pathlib import Path


def delete_empty_files(target_dir: str | Path, dry_run: bool = False) -> None:
    directory = Path(target_dir).resolve()
    if not directory.is_dir():
        print(f"Error: '{directory}' is not a valid directory.")
        return

    empty_count = 0
    deleted_count = 0

    for item in directory.rglob("*"):
        # Check that it is a regular file and not a symlink
        if item.is_file() and not item.is_symlink():
            try:
                if item.stat().st_size == 0:
                    empty_count += 1
                    if dry_run:
                        print(f"[DRY RUN] Would delete: {item}")
                    else:
                        item.unlink()
                        deleted_count += 1
                        print(f"Deleted: {item}")
            except OSError as error:
                print(f"Skipped '{item}': {error}")

    status = "Identified" if dry_run else "Successfully deleted"
    count = empty_count if dry_run else deleted_count
    print(f"\n{status} {count} empty file(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recursively scan and remove empty (0-byte) files."
    )
    parser.add_argument("folder", help="Path to the directory to scan.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files that would be removed without deleting them.",
    )

    args = parser.parse_args()
    delete_empty_files(args.folder, dry_run=args.dry_run)